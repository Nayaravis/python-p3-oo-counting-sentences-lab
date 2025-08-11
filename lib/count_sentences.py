#!/usr/bin/env python3

class MyString:
  END_PUNCTUATIONS = ".?!"
  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.check_end(".")

  def is_question(self):
    return self.check_end("?")

  def is_exclamation(self):
    return self.check_end("!")

  def count_sentences(self):
    count = 0
    for index, char in enumerate(self.value):
      if index != len(self.value) - 1:
        if index == 0:
          pass
        elif char in MyString.END_PUNCTUATIONS and self.value[index + 1] != char:
          count += 1
      else:
        if char in MyString.END_PUNCTUATIONS:
          count += 1
    
    return count

  def check_end(self, endswith):
    return True if self.value.endswith(endswith) else False
