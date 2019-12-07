#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title, set_role_source_info


class jlreqruby(nodes.General, nodes.Element, nodes.Inline):
    pass


def visit_jlreqruby(self, node):
    paren_start = self.builder.config.rubytag_start
    paren_end = self.builder.config.rubytag_end

    self.body.append('\\ruby[g]{' + node['base'])
    self.body.append('}{' + node['text'])
    self.body.append('}')
    raise nodes.SkipNode


def jlreqruby_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for rubytag."""
    text = utils.unescape(text)
    has_explicit, base, text = split_explicit_title(text)

    if not has_explicit:
        # the role does not have ruby-text is converted to Text node
        node = nodes.Text(text)
    else:
        node = jlreqruby(rawtext, base=base, text=text)

    set_role_source_info(inliner, lineno, node)
    return [node], []


def setup(app):
    app.add_role('ruby', jlreqruby_role)
    app.add_node(jlreqruby, latex=(visit_jlreqruby, None))
    app.add_config_value('rubytag_start', '(', 'latex')
    app.add_config_value('rubytag_end', ')', 'latex')
