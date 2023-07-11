 CXX ?= g++

DEBUG ?= 1
ifeq ($(DEBUG), 1)
    CXXFLAGS += -g
else
    CXXFLAGS += -O2

endif

server: main.cpp  ./timer/lst_timer.cpp ./http/http_conn.cpp ./log/log.cpp ./CGImysql/sql_connection_pool.cpp  webserver.cpp config.cpp
	$(CXX) -I/home/duanwei/anaconda3/include/python3.9 -o server  $^ $(CXXFLAGS) -lpthread -lmysqlclient -lpython3.9 -L/home/duanwei/anaconda3/lib


clean:
	rm  -r server
