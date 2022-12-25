#include <math.h>
#include <stdint.h>
#include <stdio.h>
// #include <stdlib.h>  // TODO: check if needed

#define  DEBUG(s,v)  do{if(1){printf(s, v);}}while(0)

int main() {
  char *line;
  FILE *fh = fopen("input25", "r");
  while(fh) {
    uint64_t n = 0;
    size_t len;
    getline(&line, &len, fh);
    char ch;
    do {
      uint8_t i;
      ch = line[i];
      uint8_t place = 0;
      uint64_t val;
      switch(ch) {
        case '=':
          val = -2;
          break;
        case '-':
          val = -1;
          break;
        case '0':
          val = 0;
          break;
        case '1':
          val = 1;
          break;
        case '2':
          val = 2;
          break;
      }
      n += (int)pow(5, place) * val;
    } while (ch != '\n');
    DEBUG("%lld\n", n);
  }

  fclose(fh);

  printf("Part A: %lld\n", 0);
  printf("Part B: %lld\n", 0);
}
