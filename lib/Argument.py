class Argument:
    def __init__(self,args):
        self.commands = []
        self.options = []
        self.optionValues = {} # {option: value}
        self.args = args
        print(self.args)

        for i in args:
            if i.startswith("-") or i.startswith("--"):
                #this is an option value
                if "=" in i:
                    pair = i.split('=')
                    self.optionValues[pair[0]] = pair[1]
                    self.options.append(pair[0])
            else:
                #this is a command
                self.commands.append(i)

    def hasOptions(self,options:list):
         useroption = set(self.options)
         optionset = set(options)
         return list(useroption & optionset)
    
    def hasOption(self, option):
        return option in self.hasOptions[option]
    
    def hasCommands(self,command):
        usercommands = set(self.commands)
        commandset = set(command)
        return list(usercommands & commandset) 
    def hasCommand(self,command):
        return command in self.hasCommands(command)

    def getOptionValue(self, option, default=None):
        if option in self.optionValues:
            return self.optionValues[option]
        else:
            return default
        
    def hasOptionValue(self, option):
        return option in self.optionValues
        
    

