import pymem
import pymem.process

dwEntityList = 0x4DD69DC
glowObjectManager = 0x531F608
glowIndex = 0x10488
m_bSpotted = 0x93D
model_ambient_min = 0x58F054

def mainThread():
    print("Python Glow, Chams, Radar Cheat for CS:GO ")
    print("First, set the glow color in rgb format")
    glowColorRed = input("Glow color red: ")
    glowColorGreen = input("Glow color green: ")
    glowColorBlue = input("Glow color blue: ")
    glowColorAlpha = input("Glow color alpha: ")
    procMem = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(procMem.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(procMem.process_handle, "engine.dll").lpBaseOfDll

    while True:
        procMem.write_int(engine + model_ambient_min, 70)
        glowManager = procMem.read_int(client + glowObjectManager)
        for i in range (1, 32):
            entity = procMem.read_int(client + dwEntityList + i * 0x10)
            
            if entity:
                entGlowIndex = procMem.read_int(entity + glowIndex)
                procMem.write_float(glowManager + entGlowIndex * 0x38 + 0x8, float(float(glowColorRed) / 255))
                procMem.write_float(glowManager + entGlowIndex * 0x38 + 0xC, float(float(glowColorGreen) / 255))
                procMem.write_float(glowManager + entGlowIndex * 0x38 + 0x10, float(float(glowColorBlue) / 255))
                procMem.write_float(glowManager + entGlowIndex * 0x38 + 0x14, float(float(glowColorAlpha) / 255))
                procMem.write_int(glowManager + entGlowIndex * 0x38 + 0x28, 1)
                procMem.write_int(entity + m_bSpotted,1)
            
if __name__ == '__main__':
    mainThread()