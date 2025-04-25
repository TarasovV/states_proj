# ***States transition lib***

---

## **Introduction**

  It`s simple states transition module.

  Demonstration program is located in file test.py if you want to see example of use.

  This module\`s purpose is to make simple way of synchronous programming for my projects. I\`d be glad if you find it useful in your`s.

## **How it works**
  This module has two clases:
  * `state` - class for states of your program, it has no methods, only initialisation. If you need you can use it by itself
  * `frame` - class for making and operating frame (or frames) of your program.

  In original way only `frame` class supposed to be intaracted to while `state` classe supposed to be used only by methods of `frame` class

  In other words you need to create `frame` object, that is supposed be your program\`s frame and then create and operate stetes of your program using `frame` class methods

  All created frames will be storaged in the list which is being created outside both classes

## **Class *`state`***
Class `state` made for visualisation of states structure

#### Attributes

It has attributes:
 * `state_name` - Name of state
 * `state_id` - ID number of this state
 * `start_func` - name of function that should be activated for this state

All atributes are required for initialization

#### Methods

It only has simple init function. If you want you can to use it in your way

## **Class *`frame`***
Class `frame` is main class to be interacted with

#### Attributes

It has two attributes:

  * `state_amount` - amount of states added to `States` list. It also used as for state ID when it`s being added
  * `curr_state` - ID of current state

#### Methods
  This class has several mathods:

  * `defaultMenu` - default menu funcion that shoud be replaced by your menu function
  * `__init__` - initialization function. It has only argument - `menu_func` with default value `defaultMenu`. In this argument you should type the name of your menu finction\`s name. This method creates frame, add state with name `Main menu and assigns it to your or default menu function and then sets it as current state that would be shown first in any cases
  * `addState` - creating new state, assignes it to function and adding it to the `States` list. It has arguments `state_name` and `state_func` which are both required. Function must returns integer value of next state id for correct work
  * `frameUpdate`- updates frame to state with id =`next_state_id` (default value equals 0) and launches it\`s state `start_func` via `frameFuction` method wich result is being returned
  * `frameFuction` - launches state\`s `start_func` and returns the value that was returned as result of this
