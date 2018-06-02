# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from piksi_rtk_msgs/ReceiverState_V2_3_15.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class ReceiverState_V2_3_15(genpy.Message):
  _md5sum = "88c8f10862fd18e3d9be4baddbd4a786"
  _type = "piksi_rtk_msgs/ReceiverState_V2_3_15"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Miscellaneous information form different SBP messages

# Message definition based on libsbp v2.3.15


Header header

uint8 num_sat                   # Number of satellites.
bool rtk_mode_fix 	            # 1 = Fixed, 0 = Float.
uint8[] sat                     # Constellation-specific satellite identifier.
uint8[] cn0                     # Carrier-to-Noise density. Zero implies invalid cn0 [dB Hz / 4].
uint8 system_error              # System Error Flag.
uint8 io_error                  # IO Error Flag.
uint8 swift_nap_error           # SwiftNAP Error Flag.
uint8 external_antenna_present  # External Antenna Present Flag.
uint8 num_gps_sat               # Number of GPS satellites.
uint8[] cn0_gps                 # Carrier-to-Noise density of GPS satellites. Zero implies invalid cn0 [dB Hz / 4].
uint8 num_sbas_sat              # Number of SBAS satellites.
uint8[] cn0_sbas                # Carrier-to-Noise density of SBAS satellites. Zero implies invalid cn0 [dB Hz / 4].
uint8 num_glonass_sat           # Number of GLONASS satellites.
uint8[] cn0_glonass             # Carrier-to-Noise density of GLONASS satellites. Zero implies invalid cn0 [dB Hz / 4].
string fix_mode                 # Invalid, Single Point Position (SPP), Differential GNSS (DGNSS), Float RTK, Fixed RTK.


# codes available in message "TrackingState_V2_3_15.msg"

string STR_FIX_MODE_INVALID        = Invalid
string STR_FIX_MODE_SPP            = SPP
string STR_FIX_MODE_DGNSS          = DGNSS
string STR_FIX_MODE_FLOAT_RTK      = FLOAT_RTK
string STR_FIX_MODE_FIXED_RTK      = FIXED_RTK
string STR_FIX_MODE_DEAD_RECKONING = DEAD_RECKONING
string STR_FIX_MODE_SBAS           = SBAS
string STR_FIX_MODE_UNKNOWN        = Unknown

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  # Pseudo-constants
  STR_FIX_MODE_INVALID = 'Invalid'
  STR_FIX_MODE_SPP = 'SPP'
  STR_FIX_MODE_DGNSS = 'DGNSS'
  STR_FIX_MODE_FLOAT_RTK = 'FLOAT_RTK'
  STR_FIX_MODE_FIXED_RTK = 'FIXED_RTK'
  STR_FIX_MODE_DEAD_RECKONING = 'DEAD_RECKONING'
  STR_FIX_MODE_SBAS = 'SBAS'
  STR_FIX_MODE_UNKNOWN = 'Unknown'

  __slots__ = ['header','num_sat','rtk_mode_fix','sat','cn0','system_error','io_error','swift_nap_error','external_antenna_present','num_gps_sat','cn0_gps','num_sbas_sat','cn0_sbas','num_glonass_sat','cn0_glonass','fix_mode']
  _slot_types = ['std_msgs/Header','uint8','bool','uint8[]','uint8[]','uint8','uint8','uint8','uint8','uint8','uint8[]','uint8','uint8[]','uint8','uint8[]','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,num_sat,rtk_mode_fix,sat,cn0,system_error,io_error,swift_nap_error,external_antenna_present,num_gps_sat,cn0_gps,num_sbas_sat,cn0_sbas,num_glonass_sat,cn0_glonass,fix_mode

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ReceiverState_V2_3_15, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.num_sat is None:
        self.num_sat = 0
      if self.rtk_mode_fix is None:
        self.rtk_mode_fix = False
      if self.sat is None:
        self.sat = b''
      if self.cn0 is None:
        self.cn0 = b''
      if self.system_error is None:
        self.system_error = 0
      if self.io_error is None:
        self.io_error = 0
      if self.swift_nap_error is None:
        self.swift_nap_error = 0
      if self.external_antenna_present is None:
        self.external_antenna_present = 0
      if self.num_gps_sat is None:
        self.num_gps_sat = 0
      if self.cn0_gps is None:
        self.cn0_gps = b''
      if self.num_sbas_sat is None:
        self.num_sbas_sat = 0
      if self.cn0_sbas is None:
        self.cn0_sbas = b''
      if self.num_glonass_sat is None:
        self.num_glonass_sat = 0
      if self.cn0_glonass is None:
        self.cn0_glonass = b''
      if self.fix_mode is None:
        self.fix_mode = ''
    else:
      self.header = std_msgs.msg.Header()
      self.num_sat = 0
      self.rtk_mode_fix = False
      self.sat = b''
      self.cn0 = b''
      self.system_error = 0
      self.io_error = 0
      self.swift_nap_error = 0
      self.external_antenna_present = 0
      self.num_gps_sat = 0
      self.cn0_gps = b''
      self.num_sbas_sat = 0
      self.cn0_sbas = b''
      self.num_glonass_sat = 0
      self.cn0_glonass = b''
      self.fix_mode = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2B().pack(_x.num_sat, _x.rtk_mode_fix))
      _x = self.sat
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.cn0
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_5B().pack(_x.system_error, _x.io_error, _x.swift_nap_error, _x.external_antenna_present, _x.num_gps_sat))
      _x = self.cn0_gps
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.num_sbas_sat))
      _x = self.cn0_sbas
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.num_glonass_sat))
      _x = self.cn0_glonass
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.fix_mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 2
      (_x.num_sat, _x.rtk_mode_fix,) = _get_struct_2B().unpack(str[start:end])
      self.rtk_mode_fix = bool(self.rtk_mode_fix)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.sat = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cn0 = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.system_error, _x.io_error, _x.swift_nap_error, _x.external_antenna_present, _x.num_gps_sat,) = _get_struct_5B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cn0_gps = str[start:end]
      start = end
      end += 1
      (self.num_sbas_sat,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cn0_sbas = str[start:end]
      start = end
      end += 1
      (self.num_glonass_sat,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cn0_glonass = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.fix_mode = str[start:end].decode('utf-8')
      else:
        self.fix_mode = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2B().pack(_x.num_sat, _x.rtk_mode_fix))
      _x = self.sat
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.cn0
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_5B().pack(_x.system_error, _x.io_error, _x.swift_nap_error, _x.external_antenna_present, _x.num_gps_sat))
      _x = self.cn0_gps
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.num_sbas_sat))
      _x = self.cn0_sbas
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_B().pack(self.num_glonass_sat))
      _x = self.cn0_glonass
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.fix_mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 2
      (_x.num_sat, _x.rtk_mode_fix,) = _get_struct_2B().unpack(str[start:end])
      self.rtk_mode_fix = bool(self.rtk_mode_fix)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.sat = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cn0 = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.system_error, _x.io_error, _x.swift_nap_error, _x.external_antenna_present, _x.num_gps_sat,) = _get_struct_5B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cn0_gps = str[start:end]
      start = end
      end += 1
      (self.num_sbas_sat,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cn0_sbas = str[start:end]
      start = end
      end += 1
      (self.num_glonass_sat,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.cn0_glonass = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.fix_mode = str[start:end].decode('utf-8')
      else:
        self.fix_mode = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B
_struct_5B = None
def _get_struct_5B():
    global _struct_5B
    if _struct_5B is None:
        _struct_5B = struct.Struct("<5B")
    return _struct_5B