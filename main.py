import argparse
import json
import os
import sys

# ANSI color codes for zero-dependency terminal styling
COLORS = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "CYAN": "\033[96m",
    "GREEN": "\033[92m",
    "WARNING": "\033[93m",
    "FAIL": "\033[91m",
    "ENDC": "\033[0m",
    "BOLD": "\033[1m"
}

def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "mitre_kql.json")
    try:
        with open(json_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{COLORS['FAIL']}[!] Error: mitre_kql.json not found in current directory.{COLORS['ENDC']}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"{COLORS['FAIL']}[!] Error: Invalid JSON format in mitre_kql.json.{COLORS['ENDC']}")
        sys.exit(1)

def list_techniques(data):
    print(f"\n{COLORS['HEADER']}{COLORS['BOLD']}🛡️  Available MITRE ATT&CK Techniques:{COLORS['ENDC']}\n")
    for tech_id, info in data.items():
        print(f"  {COLORS['CYAN']}{tech_id:<6}{COLORS['ENDC']} | {info['name']}")
    print(f"\n{COLORS['WARNING']}💡 Tip: Use --technique <ID> to get the KQL query (e.g., --technique T1059){COLORS['ENDC']}\n")

def get_technique(data, tech_id):
    tech_id = tech_id.upper()
    if tech_id in data:
        info = data[tech_id]
        print(f"\n{COLORS['HEADER']}{COLORS['BOLD']}🎯 Technique: {tech_id} - {info['name']}{COLORS['ENDC']}")
        print(f"{COLORS['BLUE']}📝 Description: {info['description']}{COLORS['ENDC']}")
        print(f"\n{COLORS['GREEN']}{COLORS['BOLD']}🔍 Generated KQL Query:{COLORS['ENDC']}")
        print("-" * 70)
        print(info['kql'])
        print("-" * 70)
        print(f"{COLORS['WARNING']}💡 Tip: Adjust the time range and table names based on your specific Sentinel environment.{COLORS['ENDC']}\n")
    else:
        print(f"{COLORS['FAIL']}[!] Error: Technique {tech_id} not found in database.{COLORS['ENDC']}")
        sys.exit(1)

def export_technique(data, tech_id):
    tech_id = tech_id.upper()
    if tech_id in data:
        filename = f"{tech_id}_hunting_query.kql"
        with open(filename, "w") as f:
            f.write(f"// MITRE ATT&CK: {tech_id} - {data[tech_id]['name']}\n")
            f.write(f"// Description: {data[tech_id]['description']}\n\n")
            f.write(data[tech_id]['kql'])
        print(f"{COLORS['GREEN']}[+] Successfully exported to {filename}{COLORS['ENDC']}")
    else:
        print(f"{COLORS['FAIL']}[!] Error: Technique {tech_id} not found.{COLORS['ENDC']}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="KQL-Genie: MITRE ATT&CK to Microsoft Sentinel KQL Mapper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n  python main.py --list\n  python main.py --technique T1059\n  python main.py --export T1110"
    )
    parser.add_argument("--list", action="store_true", help="List all available MITRE techniques")
    parser.add_argument("--technique", "-t", type=str, help="Get KQL for a specific MITRE technique (e.g., T1059)")
    parser.add_argument("--export", "-e", type=str, help="Export KQL query to a .kql file")
    
    args = parser.parse_args()
    data = load_data()

    if args.list:
        list_techniques(data)
    elif args.technique:
        get_technique(data, args.technique)
    elif args.export:
        export_technique(data, args.export)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()