# robot_2wd_new.py のイメージ

class DummyMotor:
    def __init__(self, name):
        self.name = name
    def enable(self): print(f"[{self.name}] Dummy Enable")
    def disable(self): print(f"[{self.name}] Dummy Disable")
    def set_speed(self, rpm): pass # 何もしない
    def run_stop(self): print(f"[{self.name}] Dummy Stop")

class Robot2WD:
    def __init__(self, port_l, port_r):
        try:
            # 本物の接続処理
            # self.motor_l = ... 
            print("Real Robot Connected")
        except Exception:
            print("!!!! Using Dummy Motors !!!!")
            self.motor_l = DummyMotor("Left")
            self.motor_r = DummyMotor("Right")

    def enable(self):
        self.motor_l.enable()
        self.motor_r.enable()
    
    def run_straight(self, rpm):
        print(f"Moving Straight at {rpm} RPM")
        # ダミーなので実際には回らないがエラーにならない