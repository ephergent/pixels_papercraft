extends CharacterBody2D

@export var speed = 300.0
@export var jump_velocity = -400.0
@export var gravity = 1200.0 # Equivalent to ProjectSettings.physics.2d.default_gravity

func _physics_process(delta):
    # Add gravity
    if not is_on_floor():
        velocity.y += gravity * delta

    # Handle Jump.
    # "ui_accept" is typically mapped to Space.
    if Input.is_action_just_pressed("ui_accept") and is_on_floor():
        velocity.y = jump_velocity
    
    # Allow jump with "ui_up" (Up arrow) as well
    if Input.is_action_just_pressed("ui_up") and is_on_floor():
        velocity.y = jump_velocity

    # Get the input direction and handle the movement/deceleration.
    # "ui_left" and "ui_right" are typically mapped to Left and Right arrow keys.
    var direction = Input.get_axis("ui_left", "ui_right")
    if direction:
        velocity.x = direction * speed
    else:
        velocity.x = move_toward(velocity.x, 0, speed) # Simple deceleration for stopping

    move_and_slide()
