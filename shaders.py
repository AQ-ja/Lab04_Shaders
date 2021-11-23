# GLSL

vertex_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec3 outColor;
out vec2 outTexCoords;

void main()
{
    vec4 norm = vec4(normal, 0.0);

    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;

    vec4 light = vec4(pointLight, 1.0);

    float intensity = dot(modelMatrix * norm, normalize(light - pos));

    gl_Position = projectionMatrix * viewMatrix * pos;

    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""

fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec3 outColor;
in vec2 outTexCoords;

uniform sampler2D tex;

void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""

#Full blanco
fragment_shader_v2 = """
#version 450
layout (location = 0) out vec4 fragColor;

in vec3 outColor;
in vec2 outTexCoords;

uniform sampler2D tex;

void main()
{
    fragColor = vec4(2, 5, 6, 9);
}
"""

# Monocromatico 
fragment_shader_v3 = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
    float color = (fragColor.x + fragColor.y + fragColor.z) / 3.0;
    fragColor = vec4(color, color, color, 1);
}
"""

# Psico
fragment_shader_v4 = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""

# Toon Shader
fragment_shader_v5 = """
#version 450
#define steps 5
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
in float intensity;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords) * (floor(intensity * steps + 0.5) / steps);
}
"""



atlantis = """
#version 450
layout(location = 0) out vec4 fragColor;


in float intensity;
in vec2 vertexTexcoords;
in vec3 fnormal;


uniform sampler2D tex;
uniform vec4 diffuse;
uniform vec4 ambient;


void main()
{
	fragColor = vec4(fnormal, 1.1);
}
"""


vertex_toon_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;

out vec3 outColor;
out vec2 outTexCoords;
out float intensity;

void main()
{
    vec4 norm = vec4(normal, 0.0);


    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;


    vec4 light = vec4(pointLight, 1.0);


    intensity = dot(modelMatrix * norm, normalize(light - pos));
    
    gl_Position = projectionMatrix * viewMatrix * pos;


    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2);
    outTexCoords = texCoords;
}
"""


vertex_try_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texcoords;


uniform mat4 theMatrix;
uniform vec3 light;
uniform float time;


out float intensity;
out vec2 vertexTexcoords;
out vec3 v3Position;
out vec3 fnormal;
out float timer;


void main()
{

	fnormal = normal;
	vertexTexcoords = texcoords;
	v3Position = position;
	timer = time;
	intensity = dot(normal, normalize(light));
	gl_Position = theMatrix * vec4(position.x, position.y, position.z, 1.0);

}
"""
