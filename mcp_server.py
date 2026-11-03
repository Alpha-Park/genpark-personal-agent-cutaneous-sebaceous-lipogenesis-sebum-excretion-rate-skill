"""
MCP Server for Cutaneous Sebaceous Lipogenesis Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import SebaceousLipogenesisClient


def main():
    client = SebaceousLipogenesisClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_sebum_kinetics",
                            "description": "Calculates Casual Sebum Level (CSL in ug/cm2) and Sebum Excretion Rate (SER in ug/cm2/h) to classify skin surface lipid barrier typing via photometric sebumetry.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "casual_sebum_level_ug_cm2": {
                                        "type": "number",
                                        "description": "Casual sebum level on unwashed skin in ug/cm2."
                                    },
                                    "reaccumulated_sebum_ug_cm2": {
                                        "type": "number",
                                        "description": "Lipid accumulated after cleansing in ug/cm2 (optional)."
                                    },
                                    "accumulation_duration_hours": {
                                        "type": "number",
                                        "description": "Duration of accumulation in hours (default: 2.0)."
                                    },
                                    "anatomical_site": {
                                        "type": "string",
                                        "description": "Measurement anatomical site (e.g. forehead, cheek, T-zone)."
                                    },
                                    "patient_age_years": {
                                        "type": "integer",
                                        "description": "Subject age in years (optional)."
                                    }
                                },
                                "required": [
                                    "casual_sebum_level_ug_cm2"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_sebum_kinetics":
                try:
                    out = client.evaluate_sebum_kinetics(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
