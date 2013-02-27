#!/usr/bin/env python

import shutil

# Setup options for display when running waf --help
def options(ctx):
	ctx.load("flambe")

# Setup configuration when running waf configure
def configure(ctx):
	ctx.load("flambe")

# Runs the build!
def build(ctx):
	if ctx.env.debug: print("This is a debug build!")
	
	classpaths = []
	
	# for p in ["./demo/src"]:
	#     classpaths.append(ctx.path.find_dir(p))
		
	# Kick off a build with the desired platforms
	# ctx(features="flambe-server",
	#     name="remoting-server", 
	# 	npm_libs="connect commander",
	# 	main="demo.devserver.RemotingServer",
	# 	classpath=classpaths,
	# 	libs="flambe nodejs nodejs_externs transition9",
	# 	target="remoting-server.js")
		
	# ctx(name="remoting-client", 
	# 	features="flambe-server",
	# 	npm_libs="connect commander",
	# 	main="demo.devserver.RemotingClient",
	# 	classpath=classpaths,
	# 	libs="flambe nodejs nodejs_externs transition9",
	# 	target="remoting-client.js")
		
	# ctx(name="websocket-server", 
	# 	features="flambe-server",
	# 	npm_libs="commander websocket",
	# 	main="demo.devserver.TestWebsocketRouter",
	# 	classpath=classpaths,
	# 	libs="flambe nodejs transition9 nodejs_externs",
	# 	target="websocket-server.js")
		
	# ctx(name="websocket-client", 
	# 	features="flambe-server",
	# 	npm_libs="commander websocket",
	# 	main="demo.devserver.TestWebsocketRouterClient",
	# 	classpath=classpaths,
	# 	libs="flambe nodejs transition9 nodejs_externs",
	# 	target="websocket-client.js")
	
	#Stand alone asset server
	ctx(name="assetserver", 
		features="flambe-server",
		npm_libs="commander websocket",
		main="flambe.server.assets.AssetServer",
		classpath=classpaths,
		libs="flambe nodejs transition9 nodejs_externs remoting node-std hxods macro-tools",
		target="assetserver.js")
	
	shutil.copy("build/assetserver-server/assetserver.js", "./assetserver.js")
	