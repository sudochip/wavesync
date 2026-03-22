import wave


obj=wave.open("sample.wav","rb")
print("Number of channels",obj.getnchannels())
print("sample width",obj.getsampwidth())
print("Number of frames",obj.getnframes())
print("Parameters",obj.getparams())

print("time",obj.getnframes()/obj.getframerate())

obj.close()


nano=print("sugar can")
