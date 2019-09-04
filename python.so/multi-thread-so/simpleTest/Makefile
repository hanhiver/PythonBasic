all: mt mt.so

mt: mt.cpp Makefile
	g++ -o mt mt.cpp -lpthread

mt.so: mt.cpp Makefile
	g++ -o mt.so -fPIC -shared -lpthread mt.cpp 

clean:
	rm -f mt mt.so

