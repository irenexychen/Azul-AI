# Azul-AI
Using neural networks to master the tile-laying game of Azul.


 ### Use PyCharm as IDE
 
 ### Install numpy 
  ``` File->Setting->Project Interpreter ```
 #### Create an virtual environment in PyCharm to specify python.exe
 https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html
 #### Run tests
 To run unit test, open Terminal window in PyCharm. Then run, i.e.
 
 ``` python -m unittest tests/triangle_plate_tests.py ```
 #### Run all tests
 run test_runner.py
 
 Note:
 ### Refer to the coding style from
 *https://github.com/google/styleguide/blob/gh-pages/pyguide.md*
 
 
 ## NEXT STEPS:
 - populate game_format.py with data
 - implement model_run.py to train with keras 
 - implement simulate_game.py to run model.py and simulate a game between two bots
 - implement scoring.py to score games made by simulate_game.py
 
 will possibly need to implement a processing python script?
 
