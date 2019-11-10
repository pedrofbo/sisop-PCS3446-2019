import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 16)

class Memory():
    memory = np.zeros(2048)

    def showMemory(self):
        col = '0 1 2 3 4 5 6 7 8 9 A B C D E F'.split()
        mem = pd.DataFrame(data=self.memory.reshape(128, 16), columns=col)
        ind = np.arange(0, 2048, 16)
        i = 0
        index = []
        for num in ind:
            index.append(hex(int(num)).upper()[2:])
            i += 1
        mem['address'] = index
        mem.set_index('address', inplace=True)
        memHex = mem.applymap(lambda x: hex(int(x)).upper()[2:])
        print(mem.head(20).applymap(lambda x: hex(int(x)).upper()[2:]))

        #return memHex

    def reset(self):
        self.memory = np.zeros(2048)

    def loadMemory(self, segmento):
        org = int(segmento[0], 16)

        for byte in segmento[1:]:
            self.memory[org] = int(byte, 16)
            org += 1
