import cProfile
import pstats
import io
import time
from functools import wraps

def profile_with_timing(sortby='cumulative'):
    def inner_profile(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            profiler = cProfile.Profile()
            start_time = time.time()
            profiler.enable()
            result = func(*args, **kwargs)
            profiler.disable()
            end_time = time.time()
            elapsed_time = end_time - start_time
            s = io.StringIO()
            ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
            ps.print_stats()
            print(s.getvalue())
            print(f"Tiempo de ejecución de {func.__name__}: {elapsed_time:.4f} segundos")
            return result
        return wrapper
    return inner_profile