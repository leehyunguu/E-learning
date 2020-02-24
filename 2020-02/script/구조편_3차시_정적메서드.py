# 정적메서드.py
class MyCalc(object):
    @staticmethod
    def my_add(x,y):
        return x+y

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

#두번째 예제는 인스턴스 생성 방법을 하나 이상 정의한 데모코드이다. 
import time 
class MyTime(object):
    def __init__(self, hour, minutes, sec):
        self.hour = hour 
        self.minutes = minutes
        self.sec = sec 

    @staticmethod
    def now():
        t = time.localtime()
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)
    @staticmethod
    def two_hours_later():
        t = time.localtime(time.time()+7200)
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)

#아래와 같이 다양한 방법으로 호출할 수 있다. 
a = MyTime(15, 30, 40)
b = MyTime.now()
c = MyTime.two_hours_later()
print("a {0}:{1}:{2}".format(a.hour, a.minutes, a.sec))
print("b {0}:{1}:{2}".format(b.hour, b.minutes, b.sec))
print("c {0}:{1}:{2}".format(c.hour, c.minutes, c.sec))
