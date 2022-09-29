""" 
	Dependency Inversion is one of the design pattern concept to make the code components to loosely coupled

	[ Ex: one class should not highly dependent on one specific class]

	This is done in the python by ABC [ making the interface ]
"""

from abc import ABC, abstractmethod

class VehicleIgnition(ABC):

	@abstractmethod
	def engine_start(self):
		pass 

	@abstractmethod
	def engine_off(self):
		pass 

class Bike(VehicleIgnition):

	def engine_start(self):
		print("Bike Engine strating....")

	def engine_off(self):
		print("Bike Engine off....")

class Aircraft(VehicleIgnition):

	def engine_start(self):
		print("Aircraft Engine strating....")

	def engine_off(self):
		print("Aircraft Engine off....")


class VPMS:

	"""
		Vehicle Power Management System
	"""

	def __init__(self, vehicle: VehicleIgnition) -> None:
		self._vehicle = vehicle
		self._power_status = False 

	def power_on(self):
		if not self._power_status:
			self._power_status = True 
			self._vehicle.engine_start()

	def power_off(self):
		if self._power_status:
			self._power_status = False 
			self._vehicle.engine_off()


if __name__ == '__main__':
	bike = Bike()
	vpms = VPMS(bike)
	vpms.power_on()
	vpms.power_off()
