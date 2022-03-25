# Copyright (c) 2022. Chauã Queirolo.
# All rights reserved.
# This file is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from argparse import ArgumentParser

import toml as toml
from jinja2 import Environment, FileSystemLoader
from unidecode import unidecode


class ResumeBuilder:

    def execute(self, template_file: str, input_file: str, output_file: str):
        # Load the input file
        content = ''
        with open(input_file) as fp:
            content = toml.load(fp)

        # Load the template file
        environment = Environment(loader=FileSystemLoader(searchpath='./template'))
        template = environment.get_template(template_file)
        template.globals['to_id'] = self.__to_id
        template.globals['type'] = type

        # Save the result file
        with open(output_file, 'w+') as fp:
            fp.write(template.render(content=content))

    @staticmethod
    def __to_id(text: str):
        return unidecode(text.replace(' ', '_').strip().lower())


def main():
    parser = ArgumentParser()
    parser.add_argument('-t',
                        default='body.html',
                        help='template file', )
    parser.add_argument('-i',
                        default='config/resume_fr.toml',
                        help='input toml file', )
    parser.add_argument('-o',
                        default='website/body_fr.html',
                        help='output html file', )

    args = parser.parse_args()

    generator = ResumeBuilder()
    generator.execute(args.t, args.i, args.o)


if __name__ == '__main__':
    main()
