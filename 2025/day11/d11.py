lines = open("d11.txt").readlines()

class Device:
    def __init__(self, name):
        self.name = name
        self.outputs = []

    def addDevice(self, device):
        self.outputs.append(device)


        

class Factory:
    def __init__(self):
        self.devices = []

    def addDevice(self, device):
        self.devices.append(device)

    def findByName(self, name):
        for device in self.devices:
            if device.name == name:
                return device
        return None

    def findYou(self):
        return self.findByName("you")


    def countPaths(self):
        startDevice = self.findYou()
        if startDevice is None:
            return 0
        allPaths = self.findPaths(startDevice)
        return len(allPaths)
    
    def findPaths(self, current_device, path=None):
        if path is None:
            path = []
        path = path + [current_device]

        if current_device.name == "out":
            return [path]

        all_paths = []
        for next_device in current_device.outputs:
            if next_device not in path:
                new_paths = self.findPaths(next_device, path)
                all_paths.extend(new_paths)

        return all_paths

    

factory = Factory()
for line in lines:
    name = line.split(":")[0].strip()
    device = Device(name)
    factory.addDevice(device)
factory.addDevice(Device("out"))

for line in lines:
    parts = line.strip().split()
    name = parts[0].strip(":")
    outputs = parts[1:]
    device = factory.findByName(name)
    outputs = [p.strip() for p in parts[1:]]  # remove extra spaces/newlines
    for o in outputs:
        out_device = factory.findByName(o)
        if out_device:
            device.addDevice(out_device)


count = factory.countPaths()
print(f"Answer: {count}")

    