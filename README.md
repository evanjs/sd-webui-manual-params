# Manual Parameters Extension
Simple extension to append a key:value to an image's generation parameters

This can be useful when running multiple sessions with similar prompts/settings that have variance in other places
An example would be img2img generations, where you might use the same prompt, but a different source image

If the outputs are archived using a program like Hydrus, it can be difficult to catalog/search for the outputs after they are imported
By allowing the user to specify a key:value pair, each session can essentially be "tagged", and Hydrus can be configured to parse said tag when importing the outputs