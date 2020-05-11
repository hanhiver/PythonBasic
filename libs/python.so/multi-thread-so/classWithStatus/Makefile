all: norm norm.so

norm: norm.cpp Makefile
	g++ -o norm norm.cpp -lpthread

norm.so: norm.cpp Makefile
	g++ -o norm.so -fPIC -shared -lpthread norm.cpp 

clean:
	rm -f norm norm.so

