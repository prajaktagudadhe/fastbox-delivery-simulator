import math
def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )
  
def normalize_warehouses(data):
    raw = data["warehouses"]
    if isinstance(raw, list):
        return {
            w["id"]: w["location"]
            for w in raw
        }
    return raw

def normalize_agents(data):
    raw = data["agents"]
    if isinstance(raw, list):
        return {
            a["id"]: a["location"]
            for a in raw
        }
    return raw
  
def normalize_packages(data):
    packages = []
    for p in data["packages"]:
        warehouse = (
            p.get("warehouse_id")
            or p.get("warehouse")
        )

        packages.append({
            "id": p["id"],
            "warehouse": warehouse,
            "destination": p["destination"]
        })

    return packages
