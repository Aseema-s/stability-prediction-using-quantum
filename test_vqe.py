import os
from vqe_module import run_vqe_from_fcidump

def test_vqe_module():
    filepath = "H2.fcidump"
    print(f"Testing real VQE module execution on {filepath}...")
    
    try:
        final_energy = run_vqe_from_fcidump(filepath)
        print(f"Success! Final Energy Outputted: {final_energy}")
    except Exception as e:
        print(f"Test failed with error: {e}")

if __name__ == "__main__":
    test_vqe_module()
