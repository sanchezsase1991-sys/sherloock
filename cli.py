import argparse
import sys
from .sherloock import Sherloock # Importa tu clase

def main():
    parser = argparse.ArgumentParser(
        description="Sherlook - Adaptive Stateless Intelligence Core"
    )
    # Lee todos los argumentos como una sola consulta
    parser.add_argument('query', 
                        type=str, 
                        nargs='+', 
                        help='El comando para el motor Sherlook')
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    full_query = " ".join(args.query)

    # Crea la instancia
    sherloock = Sherloock()
    
    # Llama al motor de razonamiento
    result = sherloock.reason(full_query)
    print(result)

if __name__ == "__main__":
    main()
