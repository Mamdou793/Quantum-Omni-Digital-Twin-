from pxr import Usd, UsdGeom, Gf, UsdPhysics
import random

class QuantumTool:
    def __init__(self, stage_path="quantum_array_sim.usda"):
        self.stage_path = stage_path

    def generate_grid(self, count=10, spacing=150):
        stage = Usd.Stage.CreateNew(self.stage_path)
        UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
        
        # Ground
        floor = UsdGeom.Plane.Define(stage, "/World/Ground")
        UsdPhysics.CollisionAPI.Apply(stage.GetPrimAtPath("/World/Ground"))

        # Array Logic
        for i in range(count):
            for j in range(count):
                path = f"/World/Qubit_{i}_{j}"
                cube = UsdGeom.Cube.Define(stage, path)
                cube.AddTranslateOp().Set(Gf.Vec3d(i * spacing, j * spacing, 500))
                
                prim = stage.GetPrimAtPath(path)
                UsdPhysics.RigidBodyAPI.Apply(prim)
                UsdPhysics.CollisionAPI.Apply(prim)

        stage.GetRootLayer().Save()
        return f"Generated {count*count} Qubits."

    def run_measurement(self):
        stage = Usd.Stage.Open(self.stage_path)
        stats = {"Alpha": 0, "Beta": 0}

        for prim in stage.Traverse():
            if "Qubit" in prim.GetName():
                is_alpha = random.choice([True, False])
                color = Gf.Vec3f(0, 1, 0) if is_alpha else Gf.Vec3f(1, 0, 0)
                
                cube_geom = UsdGeom.Cube(prim)
                cube_geom.CreateDisplayColorAttr().Set([color])
                
                if is_alpha: stats["Alpha"] += 1
                else: stats["Beta"] += 1

        stage.GetRootLayer().Save()
        return stats