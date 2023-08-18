/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.TitaniumChallengeFormGeneralRowMax;
import org.openapitools.client.model.TitaniumChallengeFormGeneralRowMaxLength;
import org.openapitools.client.model.TitaniumChallengeFormGeneralRowMin;
import org.openapitools.client.model.TitaniumChallengeFormGeneralRowMinLength;
import org.openapitools.client.model.TitaniumChallengeFormGeneralRowPrecision;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumChallengeFormGeneralRow
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-18T13:00:58.962458Z[UTC]")
public class TitaniumChallengeFormGeneralRow {
  public static final String SERIALIZED_NAME_FIELD = "field";
  @SerializedName(SERIALIZED_NAME_FIELD)
  private String field;

  public static final String SERIALIZED_NAME_MAX = "max";
  @SerializedName(SERIALIZED_NAME_MAX)
  private TitaniumChallengeFormGeneralRowMax max;

  public static final String SERIALIZED_NAME_MAX_LENGTH = "maxLength";
  @SerializedName(SERIALIZED_NAME_MAX_LENGTH)
  private TitaniumChallengeFormGeneralRowMaxLength maxLength;

  public static final String SERIALIZED_NAME_MIN = "min";
  @SerializedName(SERIALIZED_NAME_MIN)
  private TitaniumChallengeFormGeneralRowMin min;

  public static final String SERIALIZED_NAME_MIN_LENGTH = "minLength";
  @SerializedName(SERIALIZED_NAME_MIN_LENGTH)
  private TitaniumChallengeFormGeneralRowMinLength minLength;

  public static final String SERIALIZED_NAME_PRECISION = "precision";
  @SerializedName(SERIALIZED_NAME_PRECISION)
  private TitaniumChallengeFormGeneralRowPrecision precision;

  public static final String SERIALIZED_NAME_REGEX = "regex";
  @SerializedName(SERIALIZED_NAME_REGEX)
  private String regex;

  public static final String SERIALIZED_NAME_TOOLTIP = "tooltip";
  @SerializedName(SERIALIZED_NAME_TOOLTIP)
  private String tooltip;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Object value;

  public TitaniumChallengeFormGeneralRow() { 
  }

  public TitaniumChallengeFormGeneralRow field(String field) {
    
    this.field = field;
    return this;
  }

   /**
   * Get field
   * @return field
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getField() {
    return field;
  }


  public void setField(String field) {
    this.field = field;
  }


  public TitaniumChallengeFormGeneralRow max(TitaniumChallengeFormGeneralRowMax max) {
    
    this.max = max;
    return this;
  }

   /**
   * Get max
   * @return max
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumChallengeFormGeneralRowMax getMax() {
    return max;
  }


  public void setMax(TitaniumChallengeFormGeneralRowMax max) {
    this.max = max;
  }


  public TitaniumChallengeFormGeneralRow maxLength(TitaniumChallengeFormGeneralRowMaxLength maxLength) {
    
    this.maxLength = maxLength;
    return this;
  }

   /**
   * Get maxLength
   * @return maxLength
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumChallengeFormGeneralRowMaxLength getMaxLength() {
    return maxLength;
  }


  public void setMaxLength(TitaniumChallengeFormGeneralRowMaxLength maxLength) {
    this.maxLength = maxLength;
  }


  public TitaniumChallengeFormGeneralRow min(TitaniumChallengeFormGeneralRowMin min) {
    
    this.min = min;
    return this;
  }

   /**
   * Get min
   * @return min
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumChallengeFormGeneralRowMin getMin() {
    return min;
  }


  public void setMin(TitaniumChallengeFormGeneralRowMin min) {
    this.min = min;
  }


  public TitaniumChallengeFormGeneralRow minLength(TitaniumChallengeFormGeneralRowMinLength minLength) {
    
    this.minLength = minLength;
    return this;
  }

   /**
   * Get minLength
   * @return minLength
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumChallengeFormGeneralRowMinLength getMinLength() {
    return minLength;
  }


  public void setMinLength(TitaniumChallengeFormGeneralRowMinLength minLength) {
    this.minLength = minLength;
  }


  public TitaniumChallengeFormGeneralRow precision(TitaniumChallengeFormGeneralRowPrecision precision) {
    
    this.precision = precision;
    return this;
  }

   /**
   * Get precision
   * @return precision
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumChallengeFormGeneralRowPrecision getPrecision() {
    return precision;
  }


  public void setPrecision(TitaniumChallengeFormGeneralRowPrecision precision) {
    this.precision = precision;
  }


  public TitaniumChallengeFormGeneralRow regex(String regex) {
    
    this.regex = regex;
    return this;
  }

   /**
   * Get regex
   * @return regex
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getRegex() {
    return regex;
  }


  public void setRegex(String regex) {
    this.regex = regex;
  }


  public TitaniumChallengeFormGeneralRow tooltip(String tooltip) {
    
    this.tooltip = tooltip;
    return this;
  }

   /**
   * Get tooltip
   * @return tooltip
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTooltip() {
    return tooltip;
  }


  public void setTooltip(String tooltip) {
    this.tooltip = tooltip;
  }


  public TitaniumChallengeFormGeneralRow type(String type) {
    
    this.type = type;
    return this;
  }

   /**
   * Get type
   * @return type
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getType() {
    return type;
  }


  public void setType(String type) {
    this.type = type;
  }


  public TitaniumChallengeFormGeneralRow value(Object value) {
    
    this.value = value;
    return this;
  }

   /**
   * Get value
   * @return value
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getValue() {
    return value;
  }


  public void setValue(Object value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumChallengeFormGeneralRow titaniumChallengeFormGeneralRow = (TitaniumChallengeFormGeneralRow) o;
    return Objects.equals(this.field, titaniumChallengeFormGeneralRow.field) &&
        Objects.equals(this.max, titaniumChallengeFormGeneralRow.max) &&
        Objects.equals(this.maxLength, titaniumChallengeFormGeneralRow.maxLength) &&
        Objects.equals(this.min, titaniumChallengeFormGeneralRow.min) &&
        Objects.equals(this.minLength, titaniumChallengeFormGeneralRow.minLength) &&
        Objects.equals(this.precision, titaniumChallengeFormGeneralRow.precision) &&
        Objects.equals(this.regex, titaniumChallengeFormGeneralRow.regex) &&
        Objects.equals(this.tooltip, titaniumChallengeFormGeneralRow.tooltip) &&
        Objects.equals(this.type, titaniumChallengeFormGeneralRow.type) &&
        Objects.equals(this.value, titaniumChallengeFormGeneralRow.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(field, max, maxLength, min, minLength, precision, regex, tooltip, type, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumChallengeFormGeneralRow {\n");
    sb.append("    field: ").append(toIndentedString(field)).append("\n");
    sb.append("    max: ").append(toIndentedString(max)).append("\n");
    sb.append("    maxLength: ").append(toIndentedString(maxLength)).append("\n");
    sb.append("    min: ").append(toIndentedString(min)).append("\n");
    sb.append("    minLength: ").append(toIndentedString(minLength)).append("\n");
    sb.append("    precision: ").append(toIndentedString(precision)).append("\n");
    sb.append("    regex: ").append(toIndentedString(regex)).append("\n");
    sb.append("    tooltip: ").append(toIndentedString(tooltip)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("field");
    openapiFields.add("max");
    openapiFields.add("maxLength");
    openapiFields.add("min");
    openapiFields.add("minLength");
    openapiFields.add("precision");
    openapiFields.add("regex");
    openapiFields.add("tooltip");
    openapiFields.add("type");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumChallengeFormGeneralRow
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumChallengeFormGeneralRow.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumChallengeFormGeneralRow is not found in the empty JSON string", TitaniumChallengeFormGeneralRow.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumChallengeFormGeneralRow.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumChallengeFormGeneralRow` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("field") != null && !jsonObj.get("field").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `field` to be a primitive type in the JSON string but got `%s`", jsonObj.get("field").toString()));
      }
      // validate the optional field `max`
      if (jsonObj.getAsJsonObject("max") != null) {
        TitaniumChallengeFormGeneralRowMax.validateJsonObject(jsonObj.getAsJsonObject("max"));
      }
      // validate the optional field `maxLength`
      if (jsonObj.getAsJsonObject("maxLength") != null) {
        TitaniumChallengeFormGeneralRowMaxLength.validateJsonObject(jsonObj.getAsJsonObject("maxLength"));
      }
      // validate the optional field `min`
      if (jsonObj.getAsJsonObject("min") != null) {
        TitaniumChallengeFormGeneralRowMin.validateJsonObject(jsonObj.getAsJsonObject("min"));
      }
      // validate the optional field `minLength`
      if (jsonObj.getAsJsonObject("minLength") != null) {
        TitaniumChallengeFormGeneralRowMinLength.validateJsonObject(jsonObj.getAsJsonObject("minLength"));
      }
      // validate the optional field `precision`
      if (jsonObj.getAsJsonObject("precision") != null) {
        TitaniumChallengeFormGeneralRowPrecision.validateJsonObject(jsonObj.getAsJsonObject("precision"));
      }
      if (jsonObj.get("regex") != null && !jsonObj.get("regex").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `regex` to be a primitive type in the JSON string but got `%s`", jsonObj.get("regex").toString()));
      }
      if (jsonObj.get("tooltip") != null && !jsonObj.get("tooltip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tooltip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tooltip").toString()));
      }
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumChallengeFormGeneralRow.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumChallengeFormGeneralRow' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumChallengeFormGeneralRow> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumChallengeFormGeneralRow.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumChallengeFormGeneralRow>() {
           @Override
           public void write(JsonWriter out, TitaniumChallengeFormGeneralRow value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumChallengeFormGeneralRow read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumChallengeFormGeneralRow given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumChallengeFormGeneralRow
  * @throws IOException if the JSON string is invalid with respect to TitaniumChallengeFormGeneralRow
  */
  public static TitaniumChallengeFormGeneralRow fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumChallengeFormGeneralRow.class);
  }

 /**
  * Convert an instance of TitaniumChallengeFormGeneralRow to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

