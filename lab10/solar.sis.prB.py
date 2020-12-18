gravitational_constant = 6.67408E-11
"""Гравитационная постоянная G"""
def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.
    Параметры:
    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """
    body.Fx = body.Fy = 0
    for obj in space_objects:
 if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += (gravitational_constant*body.m*obj.m/r**2)*((body.x - obj.x)/r)  
        body.Fy += gravitational_constant*body.m*obj.m/r**2*((body.y - obj.y)/r)  
        body.Fx -= (gravitational_constant*body.m*obj.m/r**2)*((body.x - obj.x)/r)  
        body.Fy -= gravitational_constant*body.m*obj.m/r**2*((body.y - obj.y)/r)  


def move_space_object(body, dt):

    ax = body.Fx/body.m
    body.x += body.Vx*dt + ax/2*dt**2  
    ax = body.Fx/body.m  
    body.Vx += ax*dt
    body.x += body.Vx * dt
    
    ay = body.Fy/body.m
    body.y += body.Vy*dt + ay/2*dt**2  
    ay = body.Fy/body.m
    body.Vy += ay*dt
    body.y += body.Vy * dt

def recalculate_space_objects_positions(space_objects, dt):
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)
if __name__ == "__main__":
    print("This module is not for direct call!")