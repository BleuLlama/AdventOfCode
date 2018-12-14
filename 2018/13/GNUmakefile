
export CXXFLAGS += -DFORCE_DESKTOP -Wno-int-to-pointer-cast
export CFLAGSS += -g

export CXX := g++
export CC  := gcc

TARG := aoc

SRCS := a.c	\
		../clib/aoclib.c

OBJS := $(SRCS:%.c=%.o)

all: $(TARG)

$(TARG): $(OBJS)
	@echo link $@
	@$(CXX) $(CXXFLAGS) $^ $(LDFLAGS) $(LIBS) -o $@


%.o: %.c
	@echo build $<
	$(CC) $(CXXFLAGS) -c -o $@ $<


clean:
	@echo removing generated files
	rm -f $(OBJS) $(TARG)

run:	$(TARG)
	./$(TARG) input.txt

test:	$(TARG)
	./$(TARG) sample.txt


all2:
	python process.py

.DEFAULT:
	@echo make $@? I dunno. 
