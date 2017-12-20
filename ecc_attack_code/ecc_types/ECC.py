import abc

class ECC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_r_js(self):
        pass

    @abc.abstractmethod
    def generate_alpha_js(self):
        pass

    @abc.abstractmethod
    def generate_v_values(self):
        pass

    @abc.abstractmethod
    def get_k(self):
        pass

    @abc.abstractmethod
    def get_g(self):
        pass

    @abc.abstractmethod
    def get_t(self):
        pass
