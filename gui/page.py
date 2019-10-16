import abc
import tkinter as tk
from tkinter import ttk
import numpy as np

from .guicomponent import PageComponent, Graph
from neuralnetwork.algorithms import simpleperceptron, mlp

''' GUI function implement (Called by GUI) '''
class Pages(abc.ABC):
	def __init__(self, root):
		self.root = tk.Frame(root)
		self.neural_network = None

	@abc.abstractmethod
	def create_para_IO_frame(self):
		""" """
	@abc.abstractmethod
	def create_graph_frame(self):
		""" """
	@abc.abstractmethod
	def start_to_train(self):
		""" """
	@abc.abstractmethod
	def stop_to_start(self):
		""" """
	@abc.abstractmethod
	def finish_training(self):
		""" """

class SimplePerceptronPages(Pages):
	def __init__(self, root, dataset_list):
		super().__init__(root)
		self.create_para_IO_frame(dataset_list)
		self.create_graph_frame()
		self.root.pack(side=tk.LEFT, fill=tk.BOTH)
		
		# self.start_to_train()

	def create_para_IO_frame(self, dataset_list):
		self.IO_frame = tk.Frame(master=self.root)
		self.page_component = PageComponent(self.IO_frame, dataset_list)
		
		self.page_component.data_select()
		self.page_component.learning_rate()
		self.page_component.convergence_condition()
		self.page_component.execution_button(self.start_to_train, self.stop_to_start)
		self.page_component.training_result()
		
		self.IO_frame.pack(side=tk.LEFT, fill=tk.BOTH)

	def create_graph_frame(self):
		self.graph_frame = tk.Frame(master=self.root)
		self.graph = Graph(self.graph_frame)
		self.graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=2, pady=3)

		# self.page_component.graph_None()
		# self.page_component.graph_2D(self.root)
		# self.page_component.graph_3D()
	def start_to_train(self):
		self.page_component.print_to_result("\n\n\n=== Start to Train ===")

		self.page_component.start_to_train()
		kwargs = dict(data=self.page_component.dataset_list[self.page_component.data_selection.get()],
					  initial_learning_rate=float(self.page_component.learning_rate.get()),
					  max_epoches=int(self.page_component.max_epoches.get()),
					  least_error_rate=float(self.page_component.least_error_rate.get()),
					  )
		if (self.page_component.is_condition_max_epoches.get()==2):
			kwargs["mode"] = "least_error_rate"
		self.neural_network = simpleperceptron.SimplePerceptron(self, **kwargs)
		self.neural_network.run()

	def stop_to_start(self):
		if(self.neural_network != None):
			self.page_component.stop_to_start()
			self.neural_network.stop_training()

	def finish_training(self):
		self.page_component.finish_training()


class MLPPages(Pages):
	def __init__(self, root, dataset_list):
		super().__init__(root)
		self.create_para_IO_frame(dataset_list)
		self.create_graph_frame()
		self.root.pack(side=tk.LEFT, fill=tk.BOTH)
		
		# self.start_to_train()

	def create_para_IO_frame(self, dataset_list):
		self.IO_frame = tk.Frame(master=self.root)
		self.page_component = PageComponent(self.IO_frame, dataset_list)
		
		self.page_component.data_select()
		self.page_component.learning_rate()
		self.page_component.convergence_condition()
		self.page_component.neurons_layers()
		self.page_component.execution_button(self.start_to_train, self.stop_to_start)
		self.page_component.training_result()
		
		self.IO_frame.pack(side=tk.LEFT, fill=tk.BOTH)

	def create_graph_frame(self):
		self.graph_frame = tk.Frame(master=self.root)
		self.graph = Graph(self.graph_frame)
		self.graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=2, pady=3)

		# self.page_component.graph_None()
		# self.page_component.graph_2D(self.root)
		# self.page_component.graph_3D()
	def start_to_train(self):
		self.page_component.print_to_result("\n\n\n=== Start to Train ===")

		self.page_component.start_to_train()
		kwargs = dict(data=self.page_component.dataset_list[self.page_component.data_selection.get()],
					hidden_neurons=list(map(int, self.page_component.hidden_layer.get().split(" "))),
					initial_learning_rate=float(self.page_component.learning_rate.get()),
					max_epoches=int(self.page_component.max_epoches.get()),
					least_error_rate=float(self.page_component.least_error_rate.get()),
					)
		if (self.page_component.is_condition_max_epoches.get()==2):
			kwargs["mode"] = "least_error_rate"
		self.neural_network = mlp.MLP(self, **kwargs)
		self.neural_network.run()

	def stop_to_start(self):
		if(self.neural_network != None):
			self.page_component.stop_to_start()
			self.neural_network.stop_training()

	def finish_training(self):
		self.page_component.finish_training()