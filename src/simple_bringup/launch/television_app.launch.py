from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    remap_channel_topic = ("channel_something", "channel_something_else")

    television_node = Node(
        package='simple_py_pkg',
        executable='television_node',
        name='new_television_node',
        remappings=[remap_channel_topic],
        parameters=[
            {'greeting': 'Hello!'}
        ]
    )

    remote_controller_node = Node(
        package='simple_py_pkg',
        executable='remote_controller_node',
        name='new_remote_controller_node',
        parameters=[
            {'command_to_publish': 'Turn on the TV'}
        ],
        remappings=[remap_channel_topic]
    )

    ld.add_action(television_node)
    ld.add_action(remote_controller_node)

    return ld