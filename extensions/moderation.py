# Imports
import hikari
import lightbulb

moderation_plugin = lightbulb.Plugin("Moderation")

@moderation_plugin.command
@lightbulb.option('reason', 'Reason for kicking the user.', type = str)
@lightbulb.option('user', 'User to be kicked.', type = hikari.Member)
@lightbulb.command('kick', 'Kicks a user from the guild.')
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def kick(ctx):
    await ctx.options.user.kick(reason = ctx.options.reason)

@moderation_plugin.command
@lightbulb.option('reason', 'Reason for banning the user.', type = str)
@lightbulb.option('days_delete', 'deletes the messages specified by this property.', type = int)
@lightbulb.option('user', 'User to be banned.', type = hikari.Member)
@lightbulb.command('ban', 'Bans a user from the guild.')
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def ban(ctx):
    await ctx.options.user.ban(delete_message_days = ctx.options.days_delete, reason = ctx.options.reason)

@moderation_plugin.command
@lightbulb.option('reason', 'Reason for unbanning the user.', type = str)
@lightbulb.option('user', 'User to be unbanned.', type = hikari.Member)
@lightbulb.command('unban', 'Unbans a user from the guild.')
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def unban(ctx):
    await ctx.options.user.unban(reason = ctx.options.reason)


# Loading the plugin
def load(bot):
    bot.add_plugin(moderation_plugin)

def unload(bot):
    bot.remove_plugin(moderation_plugin)