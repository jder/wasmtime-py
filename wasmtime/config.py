from .ffi import *
from ctypes import *

dll.wasm_config_new.restype = P_wasm_config_t
dll.wasmtime_config_strategy_set.restype = c_bool
dll.wasmtime_config_profiler_set.restype = c_bool


class Config(object):
    def __init__(self):
        self.__ptr__ = dll.wasm_config_new()

    def debug_info(self, enable):
        if not isinstance(enable, bool):
            raise TypeError('expected a bool')
        dll.wasmtime_config_debug_info_set(self.__ptr__, enable)

    def wasm_threads(self, enable):
        if not isinstance(enable, bool):
            raise TypeError('expected a bool')
        dll.wasmtime_config_wasm_threads_set(self.__ptr__, enable)

    def wasm_reference_types(self, enable):
        if not isinstance(enable, bool):
            raise TypeError('expected a bool')
        dll.wasmtime_config_wasm_reference_types_set(self.__ptr__, enable)

    def wasm_simd(self, enable):
        if not isinstance(enable, bool):
            raise TypeError('expected a bool')
        dll.wasmtime_config_wasm_simd_set(self.__ptr__, enable)

    def wasm_bulk_memory(self, enable):
        if not isinstance(enable, bool):
            raise TypeError('expected a bool')
        dll.wasmtime_config_wasm_bulk_memory_set(self.__ptr__, enable)

    def wasm_multi_value(self, enable):
        if not isinstance(enable, bool):
            raise TypeError('expected a bool')
        dll.wasmtime_config_wasm_multi_value_set(self.__ptr__, enable)

    def strategy(self, strategy):
        if strategy == "auto":
            ok = dll.wasmtime_config_strategy_set(self.__ptr__, 0)
        elif strategy == "cranelift":
            ok = dll.wasmtime_config_strategy_set(self.__ptr__, 1)
        elif strategy == "lightbeam":
            ok = dll.wasmtime_config_strategy_set(self.__ptr__, 2)
        else:
            raise RuntimeError("unknown strategy: " + str(strategy))
        if not ok:
            raise RuntimeError("failed to configure strategy: " + strategy)

    def cranelift_debug_verifier(self, enable):
        if not isinstance(enable, bool):
            raise TypeError('expected a bool')
        dll.wasmtime_config_cranelift_debug_verifier_set(self.__ptr__, enable)

    def cranelift_opt_level(self, opt_level):
        if opt_level == "none":
            dll.wasmtime_config_cranelift_opt_level_set(self.__ptr__, 0)
        elif opt_level == "speed":
            dll.wasmtime_config_cranelift_opt_level_set(self.__ptr__, 1)
        elif opt_level == "speed_and_size":
            dll.wasmtime_config_cranelift_opt_level_set(self.__ptr__, 2)
        else:
            raise RuntimeError("unknown opt level: " + str(opt_level))

    def profiler(self, profiler):
        if profiler == "none":
            ok = dll.wasmtime_config_profiler_set(self.__ptr__, 0)
        elif profiler == "jitdump":
            ok = dll.wasmtime_config_profiler_set(self.__ptr__, 1)
        else:
            raise RuntimeError("unknown profiler: " + str(profiler))
        if not ok:
            raise RuntimeError("failed to configure profiler: " + profiler)

    def __del__(self):
        if hasattr(self, '__ptr__'):
            dll.wasm_config_delete(self.__ptr__)
