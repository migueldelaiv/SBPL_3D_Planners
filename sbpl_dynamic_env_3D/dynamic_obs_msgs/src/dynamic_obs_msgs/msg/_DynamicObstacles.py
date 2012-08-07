"""autogenerated by genmsg_py from DynamicObstacles.msg. Do not edit."""
import roslib.message
import struct

import dynamic_obs_msgs.msg
import geometry_msgs.msg
import std_msgs.msg

class DynamicObstacles(roslib.message.Message):
  _md5sum = "92b063c75c79b3baa03490e44c9c700b"
  _type = "dynamic_obs_msgs/DynamicObstacles"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """#an array of dynamic obstacles
Header header
DynamicObstacle[] dyn_obs

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: dynamic_obs_msgs/DynamicObstacle
#the radius of the dynamic obstacle
float64 radius

#a list of possible trajectories it may follow (with probabilities summing to 1)
DynObsTrajectory[] trajectories

================================================================================
MSG: dynamic_obs_msgs/DynObsTrajectory
#a dynamic obstacle trajectory

#the probability of the obstacle following this trajectory
float64 probability

#whether this obstacle should be treated like a static obstacle at the end of its trajectory (true) 
#or the obstacle is ignored after the end of its trajectory (false)
bool exists_after

#the time parameterized path
geometry_msgs/PoseWithCovarianceStamped[] points

================================================================================
MSG: geometry_msgs/PoseWithCovarianceStamped
# This expresses an estimated pose with a reference coordinate frame and timestamp

Header header
PoseWithCovariance pose

================================================================================
MSG: geometry_msgs/PoseWithCovariance
# This represents a pose in free space with uncertainty.

Pose pose

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['header','dyn_obs']
  _slot_types = ['Header','dynamic_obs_msgs/DynamicObstacle[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       header,dyn_obs
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(DynamicObstacles, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      if self.dyn_obs is None:
        self.dyn_obs = []
    else:
      self.header = std_msgs.msg._Header.Header()
      self.dyn_obs = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.dyn_obs)
      buff.write(_struct_I.pack(length))
      for val1 in self.dyn_obs:
        buff.write(_struct_d.pack(val1.radius))
        length = len(val1.trajectories)
        buff.write(_struct_I.pack(length))
        for val2 in val1.trajectories:
          _x = val2
          buff.write(_struct_dB.pack(_x.probability, _x.exists_after))
          length = len(val2.points)
          buff.write(_struct_I.pack(length))
          for val3 in val2.points:
            _v1 = val3.header
            buff.write(_struct_I.pack(_v1.seq))
            _v2 = _v1.stamp
            _x = _v2
            buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
            _x = _v1.frame_id
            length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _v3 = val3.pose
            _v4 = _v3.pose
            _v5 = _v4.position
            _x = _v5
            buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
            _v6 = _v4.orientation
            _x = _v6
            buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
            buff.write(_struct_36d.pack(*_v3.covariance))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.dyn_obs = []
      for i in range(0, length):
        val1 = dynamic_obs_msgs.msg.DynamicObstacle()
        start = end
        end += 8
        (val1.radius,) = _struct_d.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.trajectories = []
        for i in range(0, length):
          val2 = dynamic_obs_msgs.msg.DynObsTrajectory()
          _x = val2
          start = end
          end += 9
          (_x.probability, _x.exists_after,) = _struct_dB.unpack(str[start:end])
          val2.exists_after = bool(val2.exists_after)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.points = []
          for i in range(0, length):
            val3 = geometry_msgs.msg.PoseWithCovarianceStamped()
            _v7 = val3.header
            start = end
            end += 4
            (_v7.seq,) = _struct_I.unpack(str[start:end])
            _v8 = _v7.stamp
            _x = _v8
            start = end
            end += 8
            (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            _v7.frame_id = str[start:end]
            _v9 = val3.pose
            _v10 = _v9.pose
            _v11 = _v10.position
            _x = _v11
            start = end
            end += 24
            (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
            _v12 = _v10.orientation
            _x = _v12
            start = end
            end += 32
            (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
            start = end
            end += 288
            _v9.covariance = _struct_36d.unpack(str[start:end])
            val2.points.append(val3)
          val1.trajectories.append(val2)
        self.dyn_obs.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.dyn_obs)
      buff.write(_struct_I.pack(length))
      for val1 in self.dyn_obs:
        buff.write(_struct_d.pack(val1.radius))
        length = len(val1.trajectories)
        buff.write(_struct_I.pack(length))
        for val2 in val1.trajectories:
          _x = val2
          buff.write(_struct_dB.pack(_x.probability, _x.exists_after))
          length = len(val2.points)
          buff.write(_struct_I.pack(length))
          for val3 in val2.points:
            _v13 = val3.header
            buff.write(_struct_I.pack(_v13.seq))
            _v14 = _v13.stamp
            _x = _v14
            buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
            _x = _v13.frame_id
            length = len(_x)
            buff.write(struct.pack('<I%ss'%length, length, _x))
            _v15 = val3.pose
            _v16 = _v15.pose
            _v17 = _v16.position
            _x = _v17
            buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
            _v18 = _v16.orientation
            _x = _v18
            buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
            buff.write(_v15.covariance.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.dyn_obs = []
      for i in range(0, length):
        val1 = dynamic_obs_msgs.msg.DynamicObstacle()
        start = end
        end += 8
        (val1.radius,) = _struct_d.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.trajectories = []
        for i in range(0, length):
          val2 = dynamic_obs_msgs.msg.DynObsTrajectory()
          _x = val2
          start = end
          end += 9
          (_x.probability, _x.exists_after,) = _struct_dB.unpack(str[start:end])
          val2.exists_after = bool(val2.exists_after)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val2.points = []
          for i in range(0, length):
            val3 = geometry_msgs.msg.PoseWithCovarianceStamped()
            _v19 = val3.header
            start = end
            end += 4
            (_v19.seq,) = _struct_I.unpack(str[start:end])
            _v20 = _v19.stamp
            _x = _v20
            start = end
            end += 8
            (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
            start = end
            end += 4
            (length,) = _struct_I.unpack(str[start:end])
            start = end
            end += length
            _v19.frame_id = str[start:end]
            _v21 = val3.pose
            _v22 = _v21.pose
            _v23 = _v22.position
            _x = _v23
            start = end
            end += 24
            (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
            _v24 = _v22.orientation
            _x = _v24
            start = end
            end += 32
            (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
            start = end
            end += 288
            _v21.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
            val2.points.append(val3)
          val1.trajectories.append(val2)
        self.dyn_obs.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_d = struct.Struct("<d")
_struct_36d = struct.Struct("<36d")
_struct_dB = struct.Struct("<dB")
_struct_3I = struct.Struct("<3I")
_struct_4d = struct.Struct("<4d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")