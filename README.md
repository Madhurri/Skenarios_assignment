# Skenarios Building API Test Suite
## Background
This project is assigned by Skenario to automate following REST API endpoint:
https://api.skenarios.com/api/v1/portfolio/4116/building

Aim of the project is to test list, create and delete oprations of the building served from the above API endpoint.
More details are in _Assignment.pdf_

## Test Instructions

- API testing test cases are available in _SkenariosTestCases.pdf_ file. 
- API testing is automated using Python requests library. 
- It is in _test_demo_skenarios.py_ python source code file.
- Any Python 3+ version is expected to run the program. (To be sure, tested it in  Python 3.8.2)
- Test suite can be triggered by running the python program as below: 
``` python3 test_demo_skenarios.py```

Script outputs the test results after testing the API. If everything goes well, script output would look like below:

> ******  Get building with valid token   ******
TEST PASSED --- OK
************
> ******  Get building with invalid token   ******
TEST PASSED --- OK
************
> ******  Get building without token   ******
TEST PASSED --- OK
************
> ******  Create building with new ID   ******
TEST PASSED --- OK
************
> ******  Create building with existing ID   ******
TEST PASSED --- OK
************
> ******  Create building with invalid token   ******
TEST PASSED --- OK
************
> ******  Create building without token   ******
TEST PASSED --- OK
************
> ******  Delete building with valid ID   ******
TEST PASSED --- OK
************
> ******  Delete building with invalid ID   ******
TEST PASSED --- OK
************
> ******  Delete building with invalid Token   ******
TEST PASSED --- OK
************
> ******  Delete building without token   ******
TEST PASSED --- OK
************

## Additional Info
Behavior, response of APIs can be checked using Postman tool.
More instructions on how to use postman can be found from https://www.postman.com/.