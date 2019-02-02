# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ChannelModel2_swig', [dirname(__file__)])
        except ImportError:
            import _ChannelModel2_swig
            return _ChannelModel2_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_ChannelModel2_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ChannelModel2_swig = swig_import_helper()
    del swig_import_helper
else:
    import _ChannelModel2_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
    """high_res_timer_now() -> gr::high_res_timer_type"""
    return _ChannelModel2_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _ChannelModel2_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _ChannelModel2_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _ChannelModel2_swig.high_res_timer_epoch()
class ChannelModel2_ff(object):
    """
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of ChannelModel2::ChannelModel2_ff.

    To avoid accidental use of raw pointers, ChannelModel2::ChannelModel2_ff's constructor is in a private implementation class. ChannelModel2::ChannelModel2_ff::make is the public interface for creating new instances.

    Args:
        gt : 
        gr1 : 
        dis : 
        ampl : 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def make(gt, gr1, dis, ampl):
        """
        make(float gt, float gr1, float dis, float ampl) -> ChannelModel2_ff_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of ChannelModel2::ChannelModel2_ff.

        To avoid accidental use of raw pointers, ChannelModel2::ChannelModel2_ff's constructor is in a private implementation class. ChannelModel2::ChannelModel2_ff::make is the public interface for creating new instances.

        Args:
            gt : 
            gr1 : 
            dis : 
            ampl : 
        """
        return _ChannelModel2_swig.ChannelModel2_ff_make(gt, gr1, dis, ampl)

    make = staticmethod(make)

    def d_gt(self, gt):
        """d_gt(ChannelModel2_ff self, float gt)"""
        return _ChannelModel2_swig.ChannelModel2_ff_d_gt(self, gt)


    def gt(self):
        """gt(ChannelModel2_ff self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_gt(self)


    def d_gr1(self, gr1):
        """d_gr1(ChannelModel2_ff self, float gr1)"""
        return _ChannelModel2_swig.ChannelModel2_ff_d_gr1(self, gr1)


    def gr1(self):
        """gr1(ChannelModel2_ff self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_gr1(self)


    def d_dis(self, dis):
        """d_dis(ChannelModel2_ff self, float dis)"""
        return _ChannelModel2_swig.ChannelModel2_ff_d_dis(self, dis)


    def dis(self):
        """dis(ChannelModel2_ff self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_dis(self)


    def d_ampl(self, ampl):
        """d_ampl(ChannelModel2_ff self, float ampl)"""
        return _ChannelModel2_swig.ChannelModel2_ff_d_ampl(self, ampl)


    def ampl(self):
        """ampl(ChannelModel2_ff self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_ampl(self)

    __swig_destroy__ = _ChannelModel2_swig.delete_ChannelModel2_ff
    __del__ = lambda self: None
ChannelModel2_ff_swigregister = _ChannelModel2_swig.ChannelModel2_ff_swigregister
ChannelModel2_ff_swigregister(ChannelModel2_ff)

def ChannelModel2_ff_make(gt, gr1, dis, ampl):
    """
    ChannelModel2_ff_make(float gt, float gr1, float dis, float ampl) -> ChannelModel2_ff_sptr

    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of ChannelModel2::ChannelModel2_ff.

    To avoid accidental use of raw pointers, ChannelModel2::ChannelModel2_ff's constructor is in a private implementation class. ChannelModel2::ChannelModel2_ff::make is the public interface for creating new instances.

    Args:
        gt : 
        gr1 : 
        dis : 
        ampl : 
    """
    return _ChannelModel2_swig.ChannelModel2_ff_make(gt, gr1, dis, ampl)

class ChannelModel2_ff_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::ChannelModel2::ChannelModel2_ff)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::ChannelModel2::ChannelModel2_ff)> self) -> ChannelModel2_ff_sptr
        __init__(boost::shared_ptr<(gr::ChannelModel2::ChannelModel2_ff)> self, ChannelModel2_ff p) -> ChannelModel2_ff_sptr
        """
        this = _ChannelModel2_swig.new_ChannelModel2_ff_sptr(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __deref__(self):
        """__deref__(ChannelModel2_ff_sptr self) -> ChannelModel2_ff"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr___deref__(self)

    __swig_destroy__ = _ChannelModel2_swig.delete_ChannelModel2_ff_sptr
    __del__ = lambda self: None

    def make(self, gt, gr1, dis, ampl):
        """
        make(ChannelModel2_ff_sptr self, float gt, float gr1, float dis, float ampl) -> ChannelModel2_ff_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of ChannelModel2::ChannelModel2_ff.

        To avoid accidental use of raw pointers, ChannelModel2::ChannelModel2_ff's constructor is in a private implementation class. ChannelModel2::ChannelModel2_ff::make is the public interface for creating new instances.

        Args:
            gt : 
            gr1 : 
            dis : 
            ampl : 
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_make(self, gt, gr1, dis, ampl)


    def d_gt(self, gt):
        """d_gt(ChannelModel2_ff_sptr self, float gt)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_d_gt(self, gt)


    def gt(self):
        """gt(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_gt(self)


    def d_gr1(self, gr1):
        """d_gr1(ChannelModel2_ff_sptr self, float gr1)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_d_gr1(self, gr1)


    def gr1(self):
        """gr1(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_gr1(self)


    def d_dis(self, dis):
        """d_dis(ChannelModel2_ff_sptr self, float dis)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_d_dis(self, dis)


    def dis(self):
        """dis(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_dis(self)


    def d_ampl(self, ampl):
        """d_ampl(ChannelModel2_ff_sptr self, float ampl)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_d_ampl(self, ampl)


    def ampl(self):
        """ampl(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_ampl(self)


    def history(self):
        """history(ChannelModel2_ff_sptr self) -> unsigned int"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(ChannelModel2_ff_sptr self, int which, int delay)
        declare_sample_delay(ChannelModel2_ff_sptr self, unsigned int delay)
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(ChannelModel2_ff_sptr self, int which) -> unsigned int"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(ChannelModel2_ff_sptr self) -> int"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(ChannelModel2_ff_sptr self) -> double"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_relative_rate(self)


    def start(self):
        """start(ChannelModel2_ff_sptr self) -> bool"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_start(self)


    def stop(self):
        """stop(ChannelModel2_ff_sptr self) -> bool"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(ChannelModel2_ff_sptr self, unsigned int which_input) -> uint64_t"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(ChannelModel2_ff_sptr self, unsigned int which_output) -> uint64_t"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(ChannelModel2_ff_sptr self) -> int"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(ChannelModel2_ff_sptr self, int m)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(ChannelModel2_ff_sptr self)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(ChannelModel2_ff_sptr self) -> bool"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(ChannelModel2_ff_sptr self, int m)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(ChannelModel2_ff_sptr self) -> int"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(ChannelModel2_ff_sptr self, int i) -> long"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(ChannelModel2_ff_sptr self, long max_output_buffer)
        set_max_output_buffer(ChannelModel2_ff_sptr self, int port, long max_output_buffer)
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(ChannelModel2_ff_sptr self, int i) -> long"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(ChannelModel2_ff_sptr self, long min_output_buffer)
        set_min_output_buffer(ChannelModel2_ff_sptr self, int port, long min_output_buffer)
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(ChannelModel2_ff_sptr self, int which) -> float
        pc_input_buffers_full(ChannelModel2_ff_sptr self) -> pmt_vector_float
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(ChannelModel2_ff_sptr self, int which) -> float
        pc_input_buffers_full_avg(ChannelModel2_ff_sptr self) -> pmt_vector_float
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(ChannelModel2_ff_sptr self, int which) -> float
        pc_input_buffers_full_var(ChannelModel2_ff_sptr self) -> pmt_vector_float
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(ChannelModel2_ff_sptr self, int which) -> float
        pc_output_buffers_full(ChannelModel2_ff_sptr self) -> pmt_vector_float
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(ChannelModel2_ff_sptr self, int which) -> float
        pc_output_buffers_full_avg(ChannelModel2_ff_sptr self) -> pmt_vector_float
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(ChannelModel2_ff_sptr self, int which) -> float
        pc_output_buffers_full_var(ChannelModel2_ff_sptr self) -> pmt_vector_float
        """
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(ChannelModel2_ff_sptr self) -> float"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(ChannelModel2_ff_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(ChannelModel2_ff_sptr self)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(ChannelModel2_ff_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(ChannelModel2_ff_sptr self) -> int"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(ChannelModel2_ff_sptr self) -> int"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(ChannelModel2_ff_sptr self, int priority) -> int"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(ChannelModel2_ff_sptr self) -> std::string"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_name(self)


    def symbol_name(self):
        """symbol_name(ChannelModel2_ff_sptr self) -> std::string"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(ChannelModel2_ff_sptr self) -> io_signature_sptr"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(ChannelModel2_ff_sptr self) -> io_signature_sptr"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(ChannelModel2_ff_sptr self) -> long"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(ChannelModel2_ff_sptr self) -> basic_block_sptr"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(ChannelModel2_ff_sptr self, int ninputs, int noutputs) -> bool"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(ChannelModel2_ff_sptr self) -> std::string"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(ChannelModel2_ff_sptr self, std::string name)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(ChannelModel2_ff_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(ChannelModel2_ff_sptr self) -> swig_int_ptr"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(ChannelModel2_ff_sptr self) -> swig_int_ptr"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(ChannelModel2_ff_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _ChannelModel2_swig.ChannelModel2_ff_sptr_message_subscribers(self, which_port)

ChannelModel2_ff_sptr_swigregister = _ChannelModel2_swig.ChannelModel2_ff_sptr_swigregister
ChannelModel2_ff_sptr_swigregister(ChannelModel2_ff_sptr)


ChannelModel2_ff_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
ChannelModel2_ff = ChannelModel2_ff.make;



