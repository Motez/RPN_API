

1. Unit tests : Unit tests must be added in the modules level
3. Integrity Tests: Should add Integrity tests to test various scenarios:
    1. create a stack and push two elements 6,3 then do add operation
   2. iterate through the ALLOWED_OPERATIONS dict and make sure all supported operations work 
   3. Test Invalid Calculator Operations :
       1. Division by zero
      2. Operation with a single Operand
2. Delete stack Endpoint
2. Better Check and sanitization for posted values
3. Add _requirements.txt_ file 

4. ADD a config file which may contain :
   1. ALLOWED_OPERATIONS dict : Which will make it simple to add or remove supported operations
   2. MAX_STACK_SIZE : To be able to set a limit for stack size. It could be a negative value for no limit
   3. MAX_STACKS_NUMBER: Set a limit for stack creation