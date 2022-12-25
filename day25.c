#include <math.h>
#include <stdint.h>
#include <stdio.h>
// #include <stdlib.h>  // TODO: check if needed

#define  DEBUG(s,v)  do{if(1){printf(s, v);}}while(0)

int digit_map(char c) {
  switch(c) {
    case '=':  return -2; break;
    case '-':  return -1; break;
    case '1':  return  1; break;
    case '2':  return  2; break;
    default:   return  0; break;
  }
}

char snafu_map(int d) {
  switch(d) {
    case -2:  return '='; break;
    case -1:  return '-'; break;
    case  1:  return '1'; break;
    case  2:  return '2'; break;
    default:  return '0'; break;
  }
}

int main() {
  FILE *fh = fopen("input25", "r");

  char *line;
  size_t len;
  while(fh) {
    getline(&line, &len, fh);
    int i;
    for(i = 0; i < len; ++i) {
      if (line[i] == '\n')  { break; }
      /// printf("%c", line[i]);
    }
    uint64_t n = 0;
    for(int d=i-1, i=0; d >= 0; --d, ++i) {
      printf("%d - %d (%c)\n", (int)pow(5, i), digit_map(line[d]), line[d]);
      n += (int)pow(5, i) * digit_map(line[d]);
    }
    /// malloc();
    printf("n = %lld\n", n);

    printf("%s\n", line);
    printf("%d\n", len);
    char ch;
    do {
      uint8_t i = len;
      ch = line[i];
      uint8_t place = 0;
      uint64_t val;
      n += (int)pow(5, place) * val;
    } while (0);
    // TODO-debug } while (ch != '\n');
    DEBUG("%lld\n", n);
    break;
  }

  fclose(fh);

  printf("Part A: %lld\n", 0);
  printf("Part B: %lld\n", 0);
}
