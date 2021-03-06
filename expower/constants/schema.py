SCHEMA_BULB = \
(
    {
        'code': 'led_switch',
        'description': '',
        'icon_name': 'icon-dp_power',
        'id': 1,
        'mode': 'rw',
        'name': 'switch',
        'property': \
        {
            'type': 'bool',
        },
        'type': 'object',
    },
    {
        'code': 'work_mode',
        'description': '',
        'icon_name': 'icon-dp_mode',
        'id': 2,
        'mode': 'rw',
        'name': 'operating_mode',
        'property': \
        {
            'range': \
            (
                'white',
                'colour',
                'scene',
                'scene_1',
                'scene_2',
                'scene_3',
                'scene_4',
            ),
            'type': 'enum',
        },
        'type': 'object',
    },
    {
        'code': 'bright_value',
        'description': '',
        'icon_name': 'icon-dp_sun',
        'id': 3,
        'mode': 'rw',
        'name': 'brightness value',
        'property': \
        {
            'max': 255,
            'min': 25,
            'scale': 0,
            'step': 1,
            'type': 'value',
            'unit': '',
        },
        'type': 'object',
    },
    {
        'code': 'temp_value',
        'description': '',
        'icon_name': 'icon-dp_light',
        'id': 4,
        'mode': 'rw',
        'name': 'temperature value',
        'property': \
        {
            'max': 255,
            'min': 0,
            'scale': 0,
            'step': 1,
            'type': 'value',
            'unit': '',
        },
        'type': 'object',
    },
    {
        'code': 'colour_data',
        'description': 'rgbhsv',
        'id': 5,
        'mode': 'rw',
        'name': 'number of colour modes',
        'property': \
        {
            'maxlen': 14,
            'type': 'string',
        },
        'type': 'object',
    },
    {
        'code': 'scene_data',
        'description': 'rgbhsv',
        'id': 6,
        'mode': 'rw',
        'name': 'number of scene modes',
        'property': \
        {
            'maxlen': 14,
            'type': 'string',
        },
        'type': 'object',
    },
    {
        'code': 'flash_scene_1',
        'description': '',
        'id': 7,
        'mode': 'rw',
        'name': 'soft light scene',
        'property': \
        {
            'maxlen': 14,
            'type': 'string',
        },
        'type': 'object',
    },
    {
        'code': 'flash_scene_2',
        'description': '',
        'id': 8,
        'mode': 'rw',
        'name': 'colourful scene',
        'property': \
        {
            'maxlen': 44,
            'type': 'string',
        },
        'type': 'object',
    },
    {
        'code': 'flash_scene_3',
        'description': '',
        'id': 9,
        'mode': 'rw',
        'name': 'exciting scene',
        'property': \
        {
            'maxlen': 14,
            'type': 'string',
        },
        'type': 'object',
    },
    {
        'code': 'flash_scene_4',
        'description': '',
        'id': 10,
        'mode': 'rw',
        'name': 'wonderful scene',
        'property': \
        {
            'maxlen': 44,
            'type': 'string',
        },
        'type': 'object',
    },
)
