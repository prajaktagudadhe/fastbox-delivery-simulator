from utils import (
    distance,
    normalize_warehouses,
    normalize_agents,
    normalize_packages,
)

def nearest_agent(
    warehouse_loc,
    agents
):
    closest = None
    best = float("inf")
    for agent_id, loc in agents.items():
        d = distance(
            loc,
            warehouse_loc
        )
        if d < best:
            best = d
            closest = agent_id
        elif d == best:
            if agent_id < closest:
                closest = agent_id
    return closest

def simulate(data):
    warehouses = normalize_warehouses(data)
    agents = normalize_agents(data)
    packages = normalize_packages(data)
    report = []
    totals = {
        a: 0
        for a in agents
    }
    delivered_count = {
        a: 0
        for a in agents
    }
    for package in packages:
        warehouse_loc = warehouses[
            package["warehouse"]
        ]
        agent_id = nearest_agent(
            warehouse_loc,
            agents
        )
        start = agents[agent_id]
        destination = package["destination"]
        d1 = distance(
            start,
            warehouse_loc
        )
        d2 = distance(
            warehouse_loc,
            destination
        )
        total = d1 + d2
        totals[agent_id] += total
        delivered_count[
            agent_id
        ] += 1
        agents[agent_id] = destination
        report.append({
            "package": package["id"],
            "agent": agent_id,
            "distance": round(
                total,
                2
            ),
            "delivered": True
        })
    return (
        report,
        totals,
        delivered_count
    )

def top_performer(
    totals,
    delivered_count
):
    best = None
    for agent in totals:
        if best is None:
            best = agent
            continue
        if (
            delivered_count[agent]
            >
            delivered_count[best]
        ):
            best = agent
        elif (
            delivered_count[agent]
            ==
            delivered_count[best]
            and
            totals[agent]
            <
            totals[best]
        ):
            best = agent
    return best
