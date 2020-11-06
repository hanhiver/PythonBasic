all:test1.out test2.out test3.out

test2.out:test2.cpp
	g++ -o test2.out test2.cpp -I/home/hd275562/anaconda3/envs/py36/include/python3.6m -L/home/hd275562/anaconda3/envs/py36/lib -lpython3.6m
test1.out:test1.cpp
	g++ -o test1.out test1.cpp -I/home/hd275562/anaconda3/envs/py36/include/python3.6m -L/home/hd275562/anaconda3/envs/py36/lib -lpython3.6m
test3.out:test3.cpp
	g++ -o test3.out test3.cpp -I/home/hd275562/anaconda3/envs/py36/include/python3.6m -L/home/hd275562/anaconda3/envs/py36/lib -lpython3.6m


clean:
	rm -rf test1.out test2.out test3.out
