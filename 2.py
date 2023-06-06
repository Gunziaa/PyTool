import ctypes
import sys
import os



def run_as_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # 提升为管理员权限
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)
    else:
        # 已经具有管理员权限
        print('管理员')

if __name__ == "__main__":
    run_as_admin()

    # 在此处执行需要管理员权限的代码
    print("已获取管理员权限")
    os.system("pause")
