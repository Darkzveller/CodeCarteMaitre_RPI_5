import threading
import queue

our_plan_mid = None
ennemi_plan_mid = None
team = None
flag_done = False
new_waypoint = None
received_info = False
waypoints = None
main_loop = True
half_robot_lenght = 139
robot_angle = None

waypoint_lines = [
        [( (125+900)//2, y) for y in range((900+300)//2, (1000+1550)//2 +1)],
        [( (2100+2875)//2, y) for y in range((900+300)//2, (1000+1550)//2 +1)],
        [( x, (900+300)//2) for x in range((125+900)//2, (2100+2875)//2 + 1)],
        [( x, (1000+1550)//2) for x in range((125+900)//2, (2100+2875)//2 + 1)]
    ]

depot_points = [
                ((550+1000)//2, 30+100+half_robot_lenght),
                ((1000+1450)//2,30+100+half_robot_lenght),
                ((1000+1450)//2, 60+200+half_robot_lenght),
                ((1000+1450)//2, 90+300+half_robot_lenght),
                (3000-30-100-half_robot_lenght,(650+1100)//2),
                (3000-60-200-half_robot_lenght,(650+1100)//2),
                (3000-90-300-half_robot_lenght,(650+1100)//2),
                ((2000+2450)//2, 30+100+half_robot_lenght),
                ((1550+2000)//2,30+100+half_robot_lenght),
                ((1550+2000)//2,60+200+half_robot_lenght),
                ((1550+2000)//2,90+300+half_robot_lenght),
                (30+100+half_robot_lenght,(650+1100)//2),
                (60+200+half_robot_lenght,(650+1100)//2),
                (90+300+half_robot_lenght,(650+1100)//2)
                ]

depot_points_front_back = [
                ((550+1000)//2, 30+100),
                ((1000+1450)//2,30+100),
                ((1000+1450)//2, 60+200),
                ((1000+1450)//2, 90+300),
                (3000-30-100,(650+1100)//2),
                (3000-60-200,(650+1100)//2),
                (3000-90-300,(650+1100)//2),
                ((2000+2450)//2, 30+100),
                ((1550+2000)//2,30+100),
                ((1550+2000)//2,60+200),
                ((1550+2000)//2,90+300),
                (30+100,(650+1100)//2),
                (60+200,(650+1100)//2),
                (90+300,(650+1100)//2)
                ]

ip_dico = {
    "Matthieu" : "172.20.10.4",
    "rpi5" : None,                                                      
    "bw_16_1" : None,
    "bw_16_2" : None,
    "bw_16_3" : None,
    "bw_16_star" : "192.168.0.104"
}

conn_dico = {
    "rpi5" : None,
    "bw_16_1" : None,
    "bw_16_2" : None,
    "bw_16_3" : None,
    "bw_16_star" : None
}

front = {
    "build_state" : False,
    "position" : None
}
back = {
    "build_state" : False,
    "position" : None
} 

message_lock = threading.Lock()
client_lock = threading.Lock()
waypoint_queue = queue.Queue()
our_lock = threading.Lock()
ennemi_lock = threading.Lock()
rpi_reply = threading.Lock()
acquire_waypoint = threading.Lock()
main_loop_lock = threading.Lock()
CAN_lock = threading.Lock()
front_state_lock = threading.Lock()
back_state_lock = threading.Lock()

