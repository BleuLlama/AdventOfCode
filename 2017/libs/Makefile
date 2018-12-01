# If the first argument is "run"...
ifeq (try,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "run"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(RUN_ARGS):;@:)
endif

CMD := python
CMD := echo
TARG := process.py

all:	
	make try 1

submit:	
	make try input

try:
	@echo "Running with $(RUN_ARGS)"
	$(CMD) $(TARG) in_$(RUN_ARGS).txt

.DEFAULT:
	@echo make $@? I dunno. how about 'all' instead?

