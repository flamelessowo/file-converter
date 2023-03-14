from abc import ABC, abstractmethod, abstractstaticmethod

class FileConverter(ABC):

  @abstractstaticmethod
  def convert():
    pass