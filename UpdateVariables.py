import MainWindow as Gui


def test(root):
    print("On Thread 2")
    temperature = 1
    pressure = 2
    humidity = 3
    altitude = 4
    direction = 5
    acceleration = 6
    velocity = 7
    Gui.set_env_variables(temperature, pressure, humidity, altitude, direction, acceleration, velocity)
    Gui.update_environment()
    root.after(2000, test, root)

