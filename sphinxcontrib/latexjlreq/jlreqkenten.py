#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title, set_role_source_info


class jlreqkenten(nodes.General, nodes.Element, nodes.Inline):
    pass


def visit_jlreqkenten(self, node):
    self.body.append('\\kenten[s]{' + node['base'])
    self.body.append('}')
    raise nodes.SkipNode


def jlreqkenten_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for kententag."""
    text = utils.unescape(text)
    node = jlreqkenten(rawtext, base=text, text=text)
    set_role_source_info(inliner, lineno, node)
    return [node], []


def setup(app):
    app.add_role('kenten', jlreqkenten_role)
    app.add_node(jlreqkenten, latex=(visit_jlreqkenten, None))
