import os


train_script_path = r"/home/cailen/Projects/FractureMLDiagnosticsApp/third-party/yolov7/train.py"
test_script_path = r"test.py"

train_flags = {
    "batch": 16,
    "cfg": r"/home/cailen/Projects/FractureMLDiagnosticsApp/third-party/yolov7/cfg/training/yolov7.yaml",
    "epochs": 5,
    "data": r"/home/cailen/Projects/FractureMLDiagnosticsApp/data/data.yaml"
}

def script_executor(script_path, script_flags: dict):
    cmd = f"python {script_path}"
    for key in script_flags:
        cmd += " --" + key + f" {script_flags[key]}"
        
    os.system(cmd)


def main():
    script_executor(train_script_path, train_flags)


if __name__ == "__main__":
    main()
