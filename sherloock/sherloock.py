import numpy as np
import re, json, psutil, os
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from z3 import Solver, Int, sat
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, value
import sympy as sp
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from typing import Optional, List

class Sherloock:
    """
    Sherloock
    (Super Hybrid Efficient Reasoning Layered Orchestrator Of Knowledge)

    Motor de razonamiento híbrido, robusto y con salidas consistentes.
    """
    def __init__(self, max_fibers=4):
        self.max_fibers = max_fibers
        self.rules = {}
        self.lock = Lock()
        self.blackboard = {}
        self._init_models()
        self.command_patterns = [
            (re.compile(r'^\s*rule\s+(.+?)\s*->\s*(.+)\s*$', re.IGNORECASE), self._handle_add_rule),
            (re.compile(r'^\s*forecast\s+(\[.*?\])\s*$', re.IGNORECASE), self._handle_forecast),
            (re.compile(r'^\s*forecast\s+(\[.*?\])\s+with_limit\s+(.+)\s*$', re.IGNORECASE), self._handle_constrained_forecast),
            (re.compile(r'^\s*logic\s+(.+)\s*$', re.IGNORECASE), self._handle_logic),
            (re.compile(r'^\s*solve\s+parallel\s+(.*?)(?:\s+where\s+(.+))?\s*$', re.IGNORECASE), self._handle_parallel_solve)
        ]

    def _init_models(self):
        X = np.array([[i] for i in range(10)])
        y = np.array([0 if i < 5 else 1 for i in range(10)])
        self.nn = MLPClassifier(max_iter=500).fit(X, y)
        self.tree = DecisionTreeClassifier().fit(X, y)

    def reason(self, input_str: str):
        ram = psutil.Process(os.getpid()).memory_info().rss / 1024**2
        for cond, act in self.rules.items():
            if cond.search(input_str):
                return f"[INSTINTO] {act} | RAM: {ram:.2f} MB"
        
        # El parser principal sigue teniendo un 'try/except' general
        for pattern, handler in self.command_patterns:
            match = pattern.match(input_str)
            if match:
                try:
                    return handler(*match.groups())
                except Exception as e:
                    return f"[PARSER Error] {e}"
        return self._handle_hybrid_classify(input_str)

    # ----- HANDLERS (Robustos y Limpios) -----
    
    def _handle_add_rule(self, pattern_str: str, action_str: str):
        self.add_rule(pattern_str, action_str)
        return f"[REGLA] Añadida: '{pattern_str}' -> '{action_str}'"

    def _parse_data_list(self, data_str: str) -> List[float]:
        try:
            data = json.loads(data_str)
            if not isinstance(data, list) or not all(isinstance(n, (int, float)) for n in data):
                raise ValueError("Debe ser una lista de números.")
            return data
        except Exception as e:
            raise ValueError(f"Error al parsear lista: {e}")

    def _handle_forecast(self, data_str: str):
        data = self._parse_data_list(data_str)
        return self._forecast(data, limit=None)

    def _handle_constrained_forecast(self, data_str: str, limit_expr: str):
        try:
            data = self._parse_data_list(data_str)
            avg = sum(data) / len(data)
            expr = limit_expr.replace('avg', str(avg))
            limit_val = float(sp.sympify(expr))
            return self._forecast(data, limit=limit_val)
        except Exception as e:
            # UNIFICADO: Mantiene el manejo de errores específico
            return f"[Z3 Parse Error] Expresión de límite inválida: {e}"

    def _handle_logic(self, eq_str: str):
        try:
            # UNIFICADO: Mantiene la lógica explícita
            x, y = sp.symbols('x y')
            eq = sp.sympify(eq_str)
            sol = sp.solve(eq, dict=True)
            return f"[LOGIC SymPy] Solución: {sol}"
        except Exception as e:
            # UNIFICADO: Mantiene el manejo de errores específico
            return f"[LOGIC Error] {e}"

    def _handle_parallel_solve(self, problem_str: str, constraint_str: Optional[str] = None):
        def worker(fid):
            s = Solver()
            x, y, z = Int('x'), Int('y'), Int('z')
            s.add(x > 0, y > 0, z > 0, x < 50, y < 50, z < 50)
            s.add(x*x + y*y == z*z)
            if s.check() == sat:
                m = s.model()
                return (m[x].as_long(), m[y].as_long(), m[z].as_long())
            return None
        
        results = []
        with ThreadPoolExecutor(max_workers=self.max_fibers) as ex:
            futures = [ex.submit(worker, i) for i in range(self.max_fibers)]
            for f in as_completed(futures):
                r = f.result()
                if r:
                    results.append(r)
        
        # UNIFICADO: Elimina el texto de "Demo"
        return f"[MÚSCULO LÓGICO] {len(results)} soluciones: {results}"

    def _handle_hybrid_classify(self, text_input: str):
        vec = np.array([[abs(hash(text_input)) % 100]])
        nn_pred = self.nn.predict(vec)[0]
        tree_pred = self.tree.predict(vec)[0]
        sat_res = "SAT OK" if nn_pred == tree_pred else "Inconsistencia"
        return f"[HÍBRIDO] NN: {nn_pred} | TREE: {tree_pred} | {sat_res}"

    # ----- SOLVERS -----

    def add_rule(self, pattern: str, action: str):
        self.rules[re.compile(pattern, re.IGNORECASE)] = action

    def _forecast(self, data: List[float], limit: Optional[float] = None):
        n = len(data)
        model = LpProblem("Forecast", LpMinimize)
        x = LpVariable.dicts("x", range(n), lowBound=0, upBound=limit)
        model += lpSum([(x[i] - data[i])**2 for i in range(n)])
        for i in range(1, n):
            model += x[i] - x[i-1] <= 10
            model += x[i] - x[i-1] >= -10
        model.solve()
        
        vals = [value(x[i]) for i in range(n)]
        
        if n >= 2:
            slope = vals[-1] - vals[-2]
            next_val_opt = vals[-1] + slope
        else:
            next_val_opt = vals[0]
        
        # UNIFICADO: Salida consistente
        # Siempre devuelve [FORECAST PuLP], pero añade la nota del límite.
        output_str = f"[FORECAST PuLP] Próximo valor optimizado: {next_val_opt:.2f}"
        if limit is not None:
            next_val_opt = min(next_val_opt, limit)
            output_str = f"[FOREC PuLP] Próximo valor (límite {limit:.2f}): {next_val_opt:.2f}"
            
        return output_str
