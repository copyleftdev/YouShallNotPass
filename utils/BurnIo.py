import multiprocessing
import os
import shutil



newdir = 'tmp/'
if os.path.isdir(newdir):
    shutil.rmtree(newdir)

os.mkdir(newdir)

def worker():
    for i in range(2000):

        with open ("tmp/tempfile{}.dat".format(i),"wb") as fileout:
            fileout.write("TEST\n"*100000)

        with open("tmp/tempfile{}.dat".format(i),"rb") as rfile:
            rfile.read()




if __name__ == '__main__':
    jobs = []
    for i in range(50):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
